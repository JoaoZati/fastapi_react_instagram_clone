import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

const BASE_URL = 'http://localhost:8000'

function App() {

    const [post, setPosts] = useState([]);

    useEffect(() => {
        fetch(BASE_URL + "/post/all")
            .then(response => {
                console.log("RESPONSE: ");
                console.log(response);
                if (response.ok) {
                    return response.json()
                        .then(data => {
                            console.log("setPosts: ");
                            setPosts(data)
                            console.log("Data: ")
                            console.log(data)
                        })
                }
                throw response
            })
            .catch(error => {
                console.log("CATCH ERROR!: ");
                console.log(error);
            });
    }, []);

    return (
        "Hello Word"
    );
}

export default App;
