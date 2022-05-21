import { useEffect, useState } from "react";
import { Container, Nav, Navbar } from "react-bootstrap";
import Apis, { endpoints } from "../configs/Apis";

export default function Header(){
    const {categories, setCategories} = useState() 

    useEffect(() => {
        const loadCategories = async () => {
            let res = await Apis.get(endpoints['categories'])
            setCategories(res.data)
        }
    }, [])

    return (
        <Navbar bg="light" expand="lg">
            <Container>
                <Navbar.Brand href="#home">BookingCarManegement</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                    <Link className="nav-link" to="/">Trang chủ</Link>
                    {categories.map(c => <Link className="nav-link" to href="#link">{c.name}</Link>)}
                </Nav>
                </Navbar.Collapse>
            </Container>
            </Navbar>
    )
}