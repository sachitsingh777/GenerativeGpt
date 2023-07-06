import React, { useEffect, useState } from 'react';
import { Box, Text, VStack, Grid } from '@chakra-ui/react';

function AllOrders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await fetch('http://localhost:5000/orders');
      const data = await response.json();
      setOrders(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Box w="80%" mx="auto">
      <Text fontSize="2xl" fontWeight="bold" mb={4}>
        Order Details
      </Text>

      <Grid templateColumns="repeat(3, 1fr)" gap={4}>
        {orders.map((order) => (
          <Box key={order._id} borderWidth="1px" borderRadius="md" p={4}>
            <Text fontSize="xl" fontWeight="bold" mb={2}>
              Order #{order._id}
            </Text>
            <Text mb={2}>Customer Name: {order.customer_name}</Text>
            <Text mb={2}>Status: {order.status}</Text>

            <Text fontSize="lg" fontWeight="bold" mt={4}>
              Dishes:
            </Text>
            <VStack align="start" mt={2} spacing={1}>
              {order.dishes.map((dish, index) => (
                <Text key={index}>{`${dish.dish_name} - ₹${dish.price}`}</Text>
              ))}
            </VStack>
          </Box>
        ))}
      </Grid>
    </Box>
  );
}

export default AllOrders;
