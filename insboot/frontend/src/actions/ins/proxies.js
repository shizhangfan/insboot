import axios from 'axios';
import {
    GET_PROXIES
} from '../types';


// GET PROXIES
export const getProxies = () => dispatch => {
    axios.get('/api/ins/proxies/')
        .then(res => dispatch({
            type: GET_PROXIES,
            payload: res.data
        })).catch(err => console.log(err))
}