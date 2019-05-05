import { GET_SETTINGS } from "../types";
import axios from "axios";

export const getSettings = () => dispatch => {
  axios
    .get("/api/ins/settings/")
    .then(res =>
      dispatch({
        type: GET_SETTINGS,
        payload: res.data
      })
    )
    .catch(err => console.log(err));
};
