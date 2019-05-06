import axios from "axios";
import { GET_INS_ACCOUNTS, ADD_INS_ACCOUNT } from "../types";


// GET INS ACCOUNTS
export const getInsAccounts = () => dispatch => {
  axios
    .get("/api/ins/accounts/")
    .then(res =>
      dispatch({
        type: GET_INS_ACCOUNTS,
        payload: res.data
      })
    )
    .catch(err => console.log(err));
};


// ADD NEW INS ACCOUNT
export const addInsAccount = (account) => dispatch => {
  axios.post("/api/ins/accounts/", account)
  .then(res => dispatch({
    type: ADD_INS_ACCOUNT,
    payload: res.data
  }))
  .catch(err => console.dir(err))
}