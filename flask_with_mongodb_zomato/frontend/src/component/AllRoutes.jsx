import { Route, Routes } from "react-router-dom";
import Menu from "../pages/Menu";
import Login from "../pages/Login";
import Signup from "../pages/Signup";
import Order from "../pages/Order";
import Orderdetails from "../pages/Orderdetails";
import { Chatbot } from "./Chatbot";

const AllRoutes = () => {
    return (
        <Routes>
          <Route path="/" element={<Menu/>} />
          <Route path="/order" element={<Order/>} />
          <Route path="orderdetails" element={<Orderdetails/>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/chatbot" element={<Chatbot/>} />
        </Routes>
      
    );
  };
  
  export default AllRoutes;