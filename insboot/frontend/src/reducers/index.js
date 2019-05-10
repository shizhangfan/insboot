import {
    combineReducers
} from "redux";
import insAccounts from "./ins/accounts";
import insSettings from "./ins/settings";
import insTags from "./ins/tags";
import proxies from "./ins/proxies";

export default combineReducers({
    insAccounts,
    insSettings,
    insTags,
    proxies
});