import React, {useState, useEffect} from 'react';
import './Post.css'

const BASE_URL = 'http://localhost:8000'

function Post({ post }) {

    const [imageUrl, setImageUrl] = useState('');
    
    useEffect(() => {
        console.log("Building Post")
        console.log(post)

        if (post.image_url_type == "absolute") {
            console.log("post image url")
            console.log(post.image_url)
            setImageUrl(post.image_url)
        } else {
            setImageUrl(BASE_URL + post.image_url)
        }
    }, []);

    console.log("image URL:  ")
    console.log(imageUrl)

    return (
        <div className='post'>
            <img className='post_image' src={imageUrl}></img>
        </div>
    );
}

export default Post;
