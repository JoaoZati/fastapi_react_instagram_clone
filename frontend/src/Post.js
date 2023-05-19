import React, {useState, useEffect} from 'react';
import './Post.css'

const BASE_URL = 'http://localhost:8000'

function Post({ post }) {

    const [imageUrl, setImageUrl] = useState('');
    const [comments, setComments] = useState([]);
    
    
    useEffect(() => {
        if (post.image_url_type == "absolute") {
            setImageUrl(post.image_url)
        } else {
            setImageUrl(BASE_URL + post.image_url)
        }
    }, []);

    useEffect(() => {
        console.log("UseEffect2: ")
        var commentsElements = [] 
        
        for (let i = 0; i < post.comments.length; i++) {
            commentsElements.push(
                <p>
                    <strong>{post.comments[i].username}: </strong> {post.comments[i].text}
                </p>
            )
        }

        setComments(commentsElements)
        console.log("comments: ")
        console.log(comments)
    }, []);

    return (
        <div className='post'>
            <img className='post_image' src={imageUrl}></img>

            <h4 className='post_text'>{post.caption}</h4>
            <div className="post_comments">
                {comments}
            </div>
        </div>
    );
}

export default Post;
