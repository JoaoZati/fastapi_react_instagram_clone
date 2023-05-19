import React, { useState, useEffect } from 'react';
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
        const generateCommentElements = () => {
            return post.comments.map((comment, index) => (
                <p key={index}>
                    <strong>{comment.username}: </strong> {comment.text}
                </p>
            ));
        };

        const renderComments = () => {
            const commentElements = generateCommentElements();

            if (commentElements.length > 0) {
                return (
                    <div className="post_comments">
                        {commentElements}
                    </div>
                );
            }

            return null;
        };

        setComments(renderComments());
    }, [post.comments]);

    return (
        <div className='post'>
            <img className='post_image' src={imageUrl}></img>

            {comments}
        </div>
    );
}

export default Post;
