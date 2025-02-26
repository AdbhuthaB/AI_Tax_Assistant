

import React, { useState } from "react";

function App() {
    const [file, setFile] = useState(null);
    const [text, setText] = useState("");

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("http://localhost:8000/extract-text/", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();
        setText(data.extracted_text);
    };

    return (
        <div>
            <h1>AI-Powered Tax Assistant</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            <pre>{text}</pre>
        </div>
    );
}

export default App;
