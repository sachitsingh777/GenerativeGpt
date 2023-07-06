import { Route, Routes } from "react-router-dom";
import Login from "../pages/Login";
import Signup from "../pages/Signup";
import AllOrders from "../pages/AllOrders";
import Orders from "../pages/Orders";
import Home from "../pages/Home";

const AllRoutes = () => {
    return (
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/order" element={<Orders/>} />
          <Route path="orderdetails" element={<AllOrders/>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      
    );
  };
  
  export default AllRoutes;