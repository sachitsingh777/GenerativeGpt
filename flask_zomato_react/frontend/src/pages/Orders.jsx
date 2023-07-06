import React, { useEffect, useState } from 'react';
import {
  Box,
  VStack,
  Grid,
  Image,
  Text,
  Checkbox,
  Button,
  FormControl,
  FormLabel,
  Input,
  useToast,
} from '@chakra-ui/react';

function Orders() {
  const [menu, setMenu] = useState([]);
  const [customerName, setCustomerName] = useState('');
  const [selectedDishes, setSelectedDishes] = useState([]);
  const toast = useToast();

  useEffect(() => {
    fetchMenu();
  }, []);

  const fetchMenu = async () => {
    try {
      const response = await fetch('http://localhost:5000/menu');
      const data = await response.json();
      const filteredMenu = data.filter((dish) => dish.stock > 0);
      setMenu(filteredMenu);
    } catch (error) {
      console.log(error);
    }
  };

  const handleCheckboxChange = (dishId) => {
    const isChecked = selectedDishes.includes(dishId);
    const updatedSelectedDishes = isChecked
      ? selectedDishes.filter((id) => id !== dishId)
      : [...selectedDishes, dishId];
    setSelectedDishes(updatedSelectedDishes);
  };

  const placeOrder = async () => {
    if (!customerName || selectedDishes.length === 0) {
      toast({
        title: 'Incomplete Order',
        description: 'Please provide your name and select at least one dish.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/take-order', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          customer_name: customerName,
          dish_ids: selectedDishes,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        toast({
          title: 'Order Placed',
          description: 'Your order has been placed successfully.',
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
        setCustomerName('');
        setSelectedDishes([]);
      } else {
        toast({
          title: 'Error',
          description: data.error || 'An error occurred while placing the order.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    } catch (error) {
      console.log(error);
      toast({
        title: 'Error',
        description: 'An error occurred while placing the order.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box w="80%" mx="auto">
      <FormControl mb={4}>
        <FormLabel htmlFor="customerName">Customer Name</FormLabel>
        <Input
          id="customerName"
          placeholder="Enter your name"
          value={customerName}
          onChange={(e) => setCustomerName(e.target.value)}
        />
      </FormControl>

      <Grid templateColumns="repeat(5, 1fr)" gap={2}>
        {menu.map((dish) => (
          <Box key={dish._id} borderWidth="1px" borderRadius="md" p={2}>
            <Image src={dish.image} alt={dish.dish_name} h={120} objectFit="cover" mb={1} />
            <Text fontWeight="bold" fontSize="md" mt={1}>
              {dish.dish_name}
            </Text>
            <Text>₹{dish.price}/-</Text>
            <Checkbox
              mt={1}
              isChecked={selectedDishes.includes(dish._id)}
              onChange={() => handleCheckboxChange(dish._id)}
            >
              Select
            </Checkbox>
          </Box>
        ))}
      </Grid>

      <Button colorScheme="blue" mt={4} onClick={placeOrder}>
        Place Order
      </Button>
    </Box>
  );
}

export default Orders;
