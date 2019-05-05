import axios from "axios";
import { GET_INS_ACCOUNTS } from "../types";

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
