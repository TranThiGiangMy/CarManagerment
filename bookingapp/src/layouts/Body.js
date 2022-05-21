import { BrowserRouter, Switch, Route } from "react-router-dom"
import Header from "./Header"
import Footer from "./Footer"
import Home from "../pages/Home"

export default function Body(){
    return (
        <>
            <BrowserRouter>
                <Header />
                <Switch>
                    <Route exact path="/" component = {Home} />
                </Switch>
                <Footer />
            </BrowserRouter>
        </>
    )
}