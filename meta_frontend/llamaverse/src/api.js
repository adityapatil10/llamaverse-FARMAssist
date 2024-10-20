import axios from 'axios';


export const getQueryResponse=async(query)=>{
    let url="http://127.0.0.1:5000/offline_answer"
    try {
        const formdata= new FormData()
        formdata.append("query",query) 
        return await axios.post(url, formdata).then((action)=>{console.log("action",action.data.prediction);return(action.data.prediction)});
        ; // Assuming the API returns a response in data
      } catch (err) {
        return("something went wrong");
        // console.error(err);
      }
}

export const getDiseaseDetails=async(file)=>{
    let url="http://127.0.0.1:5000/disease_detection"
    try {
        const formdata= new FormData()
        formdata.append("image",file) 
        return await axios.post(url, formdata).then((action)=>{console.log("action",action.data.prediction);return(action.data.prediction)});
        ; // Assuming the API returns a response in data
      } catch (err) {
        return("something went wrong");
        // console.error(err);
      }
}

export const getcropRecomend=async(file,location,month)=>{
    let url="http://127.0.0.1:5000/predict"
    try {
        const formdata= new FormData()
        formdata.append("image",file)
        formdata.append("location",location)
        formdata.append("month",month) 
        return await axios.post(url, formdata).then((action)=>{console.log("action",action.data.prediction);return(action.data.prediction)});
        ; // Assuming the API returns a response in data
      } catch (err) {
        return("something went wrong");
        // console.error(err);
      }
}

export const convertHindi=async(text)=>{
    let url="http://127.0.0.1:5000/hindi_conversation"
    try {
        const formdata= new FormData()
        formdata.append("text",text)
        return await axios.post(url, formdata).then((action)=>{console.log("action",action.data.prediction);return(action.data.prediction)});
        ; // Assuming the API returns a response in data
      } catch (err) {
        return("something went wrong");
        // console.error(err);
      }
}