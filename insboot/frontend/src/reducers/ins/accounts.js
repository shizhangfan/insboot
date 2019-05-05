import { GET_INS_ACCOUNTS } from "../../actions/types";

const initialState = {
  insAccounts: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_INS_ACCOUNTS:
      return {
        ...state,
        insAccounts: action.payload
      };
    default:
      return state;
  }
}
