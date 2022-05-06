import React, { useState } from 'react'
import './Upload.css'

const Upload = () => {

    const [file, setFile] = useState();

    const handleChange = (event) => {
        setFile(URL.createObjectURL(event.target.files[0]))
    }

    return (
        <>
            <input className='img_choose' type="file" onChange={handleChange} />
            <img src={file} className='prev_img' alt='img' />
            <button className='btn_upload'>Upload</button>
        </>
    );
}


export default Upload