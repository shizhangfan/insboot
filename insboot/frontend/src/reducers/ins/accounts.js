import { GET_INS_ACCOUNTS, ADD_INS_ACCOUNT, DELETE_INS_ACCOUNT, UPDATE_INS_ACCOUNT, SELECT_INS_ACCOUNT } from "../../actions/types";

const initialState = {
  insAccounts: [],
  currentAccount: {}
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
        insAccounts: [...state.insAccounts, action.payload],
        currentAccount: action.payload
      };
    case DELETE_INS_ACCOUNT:
      return {
        ...state,
        insAccounts: state.insAccounts.filter(a => a.id !== action.payload)
      };
    case UPDATE_INS_ACCOUNT:
      const oldAccounts = state.insAccounts.filter(a => a.id !== action.payload.id);
      return {
        ...state,
        insAccounts: [action.payload, ...oldAccounts],
        currentAccount: {}
      };
    case SELECT_INS_ACCOUNT:
      return {
        ...state,
        currentAccount: action.payload
      }
    default:
      return state;
  }
}
