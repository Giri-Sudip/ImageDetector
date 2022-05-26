import React, { useState } from 'react'
import './Upload.css'
import axios from 'axios';

const Upload = () => {
    const [File, setFile] = useState();
    const [fileURL, setFileURL] = useState();




    const handleChange = (event) => {

        setFile((event.target.files[0]))

        setFileURL(URL.createObjectURL(event.target.files[0]))


    }
    const submitForm = () => {
        const formData = new FormData();
        formData.append('file', File);


        axios
            .post('http://127.0.0.1:8000/images', formData, {
                headers: {
                    accept: 'multipart/form-data',
                }

            })

            .then(() => {
                alert('file upload succcess');
            })
            .catch(() => alert("File Upload Error"))
        return formData


    }


    return (
        <>
            <input className='img_choose' type="file" onChange={handleChange} />
            <img src={fileURL} className='prev_img' alt='img' />
            <button className='btn_upload' onClick={submitForm}>Upload</button>
        </>
    );
}


export default Upload