import axios from "axios";
import { GET_INS_ACCOUNTS, ADD_INS_ACCOUNT, DELETE_INS_ACCOUNT, SELECT_INS_ACCOUNT, UPDATE_INS_ACCOUNT } from "../types";


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

// DELETE INS ACCOUNT
export const deleteInsAccount = id => dispatch => {
  axios.delete(`/api/ins/accounts/${id}/`,)
    .then(res => dispatch({
    type: DELETE_INS_ACCOUNT,
    payload: id
  }))
  .catch(err => console.log(err))
}

// UPDATE INS ACCOUNT
export const updateInsAccount = account => dispatch => {
  axios.put(`/api/ins/accounts/${account.id}/`, account)
    .then(res => dispatch({
      type: UPDATE_INS_ACCOUNT,
      payload: account
    }))
    .catch(err => console.dir(err))
}

export const selectInsAccount = account => dispatch => {
  dispatch({
    type: SELECT_INS_ACCOUNT,
    payload: account
  })
}