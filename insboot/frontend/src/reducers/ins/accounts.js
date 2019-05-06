import { GET_INS_ACCOUNTS, ADD_INS_ACCOUNT } from "../../actions/types";

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
    case ADD_INS_ACCOUNT:
      return {
        ...state,
        insAccounts: [...state.insAccounts, action.payload]
      }
    default:
      return state;
  }
}
