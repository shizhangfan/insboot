import {
    GET_PROXIES
} from "../../actions/types"


const initialState = {
    proxies: []
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_PROXIES:
            return {
                ...state,
                proxies: action.payload
            };
        default:
            return state;
    }
}