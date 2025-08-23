# How to Run the Frontend

This document provides detailed instructions on how to set up and run the React frontend of this project.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Node.js**: [https://nodejs.org/](https://nodejs.org/)
*   **npm** (Node Package Manager), which is included with Node.js

## Getting Started

Follow these steps to get the frontend development server running:

1.  **Navigate to the frontend directory:**
    Open your terminal and change your directory to the `react_frontend` folder:
    ```bash
    cd react_frontend
    ```

2.  **Install dependencies:**
    Install all the necessary project dependencies by running the following command:
    ```bash
    npm install
    npm install react-router-dom
    ```

3.  **Start the development server:**
    Once the dependencies are installed, you can start the development server with:
    ```bash
    npm run dev
    ```
    This will start the application in development mode. You can view it in your browser at the address provided in the terminal output (usually `http://localhost:5173`).

## Building for Production

When you are ready to create a production build of the application, you can run the following command:

```bash
npm run build
```

This will create a `dist` folder in the `react_frontend` directory with the optimized and minified files for production deployment.
