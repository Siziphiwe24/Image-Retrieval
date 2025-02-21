import React from "react";

const ImageResults = ({ images }) => {
    return (
        <div>
            <h2>Search Results</h2>
            {images.length === 0 ? (
                <p>No results found.</p>
            ) : (
                <div className="image-results">
                    {images.map((img, idx) => (
                        <img key={idx} src={`http://localhost:5000/images/${img.path}`} alt={`Result ${idx + 1}`} style={{ width: "200px" }} />
                    ))}
                </div>
            )}
        </div>
    );
};

export default ImageResults;

