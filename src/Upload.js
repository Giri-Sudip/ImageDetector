import React, { useState } from 'react'
import './Upload.css'
import axios from 'axios';

const Upload = () => {
    const [file, setFile] = useState();



    const handleChange = (event) => {
        setFile(URL.createObjectURL(event.target.files[0]))
    }
    const submitForm = () => {
        const formData = new FormData();
        formData.append('file', file);
        

        axios
            .post('http://127.0.0.1:8000/images/', formData)
            console.log(formData)
            
            .then((_res) => {
                alert('file upload succcess');
            })
            .catch((err) => alert("File Upload Error"))

    }


    return (
        <>
            <input className='img_choose' type="file" onChange={handleChange} />
            <img src={file} className='prev_img' alt='img' />
            <button className='btn_upload' onClick={submitForm}>Upload</button>
        </>
    );
}


export default Upload