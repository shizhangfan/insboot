import { GET_INS_TAGS } from "../../actions/types";

const initialState = {
  insTags: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_INS_TAGS:
      return {
        ...state,
        insTags: action.payload
      };
    default:
      return state;
  }
}
