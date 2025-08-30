<script lang="ts">
  import PreviewCard from './PreviewCard.svelte';

  let linkInput = '';
  let resultOutput: string | null = null;
  let previewData: any = null; // To store metadata for the preview card
  let isLoading = false;
  let currentAction = '';

  // CORRECTED URL with the '3' added back in
  const API_BASE_URL = 'https://userusman123-smart-link-api.hf.space';

  async function handleApiCall(endpoint: string) {
    if (!linkInput) {
      resultOutput = 'Please enter a link first.';
      previewData = null;
      return;
    }

    isLoading = true;
    resultOutput = null;
    previewData = null;
    currentAction = endpoint;

    try {
      const response = await fetch(API_BASE_URL + endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: linkInput }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'An unknown error occurred.');
      }

      if (endpoint === '/qrcode') {
        const imageBlob = await response.blob();
        const imageUrl = URL.createObjectURL(imageBlob);
        resultOutput = `<img src="${imageUrl}" alt="Generated QR Code" class="qr-code-img" />`;
      } else if (endpoint === '/preview') {
        previewData = await response.json();
      } else {
        const data = await response.json();
        resultOutput = JSON.stringify(data, null, 2);
      }
    } catch (error) {
      if (error instanceof Error) {
        resultOutput = `Error: ${error.message}`;
      } else {
        resultOutput = 'An unexpected error occurred.';
      }
    } finally {
      isLoading = false;
    }
  }
</script>

<main>
  <div class="container">
    <h1>Smart Link Manager</h1>
    <p>Clean, expand, and manage your links with the power of AI.</p>

    <div class="input-group">
      <input type="text" bind:value={linkInput} placeholder="Enter a link..." />
    </div>

    <div class="button-group">
      <button on:click={() => handleApiCall('/preview')}>Preview Link 👁️</button>
      <button on:click={() => handleApiCall('/correct')}>Correct Link ✨</button>
      <button on:click={() => handleApiCall('/shorten')}>Shorten Link ✂️</button>
      <button on:click={() => handleApiCall('/qrcode')}>Get QR Code 🔳</button>
    </div>

    <div class="results-container">
      {#if isLoading}
        <p>Loading...</p>
      {:else if previewData}
        <PreviewCard data={previewData} />
      {:else if resultOutput}
        <pre>{@html resultOutput}</pre>
      {:else}
        <p>Results will be shown here...</p>
      {/if}
    </div>
  </div>
</main>

<style>
  :global(body) {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #f0f2f5;
    color: #1c1e21;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
  :global(.qr-code-img) {
    display: block;
    margin: 0 auto;
    max-width: 200px;
  }

  .container {
    background: #ffffff;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
    text-align: center;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }

  p {
    color: #606770;
    margin-bottom: 2rem;
  }

  .input-group input {
    width: calc(100% - 24px);
    padding: 12px;
    font-size: 1rem;
    border-radius: 8px;
    border: 1px solid #dddfe2;
    margin-bottom: 1rem;
  }

  .button-group {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }

  .button-group button {
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 8px;
    background-color: #e7f3ff;
    color: #1877f2;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .button-group button:hover {
    background-color: #d1e6ff;
  }

  .results-container {
    background: #f7f7f7;
    padding: 20px;
    border-radius: 8px;
    min-height: 100px;
    text-align: left;
    word-wrap: break-word;
  }
  
  pre {
    font-family: 'Courier New', Courier, monospace;
    white-space: pre-wrap;
  }
</style>