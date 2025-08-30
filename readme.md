🔗 Smart Link Manager
An intelligent, all-in-one tool to correct, preview, shorten, and generate QR codes for your links, powered by AI.

This full-stack application provides a seamless user experience for managing URLs, with a unique AI-powered feature to fix broken or mistyped links.

✨ Live Demo
Frontend (Vercel): https://smart-link-manager.vercel.app/

Backend API Docs (Hugging Face): https://userusman123-smart-link-api.hf.space/docs

🚀 Features
AI Link Correction: Automatically fixes common typos and errors in URLs (e.g., gogle.cm becomes google.com).

Link Preview: Generates a rich preview card for any link, showing its title, description, and preview image.

URL Shortening: Instantly shortens long URLs using the TinyURL service.

QR Code Generation: Creates a downloadable QR code for any link on the fly.

📸 Screenshots
(Add your screenshots of the application here. You can drag and drop them into this README on GitHub.)

[Your Screenshot Here]

🤔 What Makes This Different?
While many tools can shorten links or create QR codes, the Smart Link Manager stands out with its intelligent AI-powered correction. Most tools will simply fail if a user enters a slightly incorrect URL. This application uses Google's Gemini model to understand the user's intent and provide a corrected, functional link, saving time and reducing frustration.

🛠️ How It's Made: Tech Stack & Tools
This project is a modern full-stack application, separating the backend logic from the frontend user interface.

Backend (/backend)
Framework: FastAPI (Python) - For building a high-performance, modern, and well-documented API.

AI Model: Google Gemini API (gemini-1.5-flash-latest) - Used for the core link correction feature.

Web Scraping: Beautiful Soup - To parse HTML and extract metadata for the link preview feature.

Deployment: Hugging Face Spaces (with a custom Dockerfile) - For hosting the live Python API.

Frontend (/frontend)
Framework: SvelteKit - A modern, fast, and component-based framework for building web applications.

Language: TypeScript - For adding type safety and improving code quality.

Styling: Plain CSS with a focus on a clean, modern UI.

Deployment: Vercel - For continuous, high-performance hosting of the frontend application.

Development Tools
Code Editor: Visual Studio Code

Version Control: Git & GitHub

Terminal: Git Bash

Package Manager: npm

🌟 Give it a Star!
If you found this project useful or interesting, please consider giving it a star on GitHub! ⭐