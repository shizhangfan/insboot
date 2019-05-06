import axios from "axios";

import { GET_INS_TAGS } from "../types";

// GET INS TAGS
export const getInsTags = () => dispatch => {
  axios
    .get("/api/ins/tags/")
    .then(res =>
      dispatch({
        type: GET_INS_TAGS,
        payload: res.data
      })
    )
    .catch(err => console.log(err));
};
