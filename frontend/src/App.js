import React, { useState, useEffect } from 'react';
import './App.css';
import Post from './Post';

const BASE_URL = 'http://localhost:8000'

function App() {

    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetch(BASE_URL + "/post/all")
            .then(response => {
                // console.log("RESPONSE: ");
                // console.log(response);
                if (response.ok) {
                    return response.json()
                        .then(data => {
                            setPosts(data)
                            // console.log("Data: ")
                            // console.log(data)
                        })
                }
                throw response
            })
            .catch(error => {
                console.log("CATCH ERROR!: ");
                console.log(error);
            });
    }, []);

    var postCards = [];
    for (let i=0; i<posts.length; i++) {

        postCards.push(
            <Post post = {posts[i]}/>
        )
    }

    return (
        <div className='app_posts'>
            {postCards}
        </div>
        
    );
}

export default App;
