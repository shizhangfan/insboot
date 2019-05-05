import { combineReducers } from "redux";
import insAccounts from "./ins/accounts";
import insSettings from "./ins/settings";

export default combineReducers({ insAccounts, insSettings });
