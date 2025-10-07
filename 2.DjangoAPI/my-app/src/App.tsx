import './App.css'
import UserListItem from "./pages/users/UserListPage/UserListItem.tsx";
import {Route, Routes} from "react-router";
import UserRegisterPage from "./pages/users/UserRegisterPage";
function App() {

    return (
        <>
            <Routes>
                <Route path = {"/"}>
                    <Route index element={<UserListItem/>}></Route>
                    <Route path={"register"} element={<UserRegisterPage />}/>
                </Route>
            </Routes>
        </>
    )
}

export default App