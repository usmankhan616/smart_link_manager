<script lang="ts">
  export let data: {
    title: string;
    description: string;
    image: string | null;
    url: string;
  };
</script>

<a href={data.url} target="_blank" rel="noopener noreferrer" class="card-link">
  <div class="preview-card">
    {#if data.image}
      <img src={data.image} alt={data.title} class="preview-image" />
    {/if}
    <div class="preview-content">
      <div class="preview-title">{data.title}</div>
      <div class="preview-description">{data.description}</div>
      <div class="preview-url">{data.url}</div>
    </div>
  </div>
</a>

<style>
  .card-link {
    text-decoration: none;
    color: inherit;
  }
  .preview-card {
    border: 1px solid #dddfe2;
    border-radius: 8px;
    overflow: hidden;
    transition: box-shadow 0.2s;
  }
  .preview-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  .preview-image {
    width: 100%;
    max-height: 250px;
    object-fit: cover;
    display: block;
  }
  .preview-content {
    padding: 15px;
  }
  .preview-title {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 5px;
  }
  .preview-description {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 0.9rem;
    color: #606770;
    margin-bottom: 10px;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .preview-url {
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.8rem;
    color: #90949c;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>