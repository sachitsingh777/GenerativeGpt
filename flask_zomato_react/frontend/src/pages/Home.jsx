import React, { useState, useEffect } from 'react';
import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Switch,
  Input,
  Table,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
  useToast,
} from '@chakra-ui/react';
import axios from 'axios';

const Home = () => {
  const toast = useToast();
  const [menu, setMenu] = useState({ menu: [] });
  const [searchQuery, setSearchQuery] = useState('');
  const [newDish, setNewDish] = useState({ dish_name: '', price: '', availability: false });

  useEffect(() => {
    fetchMenu();
  }, []);

  const fetchMenu = async () => {
    try {
      const response = await axios.get('http://localhost:5000/menu');
      setMenu(response.data);
    } catch (error) {
      console.error(error);
      toast({
        title: 'Error',
        description: 'Failed to fetch menu. Please try again later.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
  };
console.log(menu)
  const handleAvailabilityToggle = async (dishId, availability) => {
    try {
      const response = await axios.post('http://localhost:5000/update_availability', {
        dish_id: dishId,
        availability: availability ? 'yes' : 'no',
      });
      setMenu(response.data);
      toast({
        title: 'Success',
        description: `Dish availability updated.`,
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error(error);
      toast({
        title: 'Error',
        description: 'Failed to update dish availability. Please try again.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
  };

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleAddDish = async () => {
    try {
      const response = await axios.post('http://localhost:5000/add_dish', newDish);
      setMenu(response.data);
      setNewDish({ dish_name: '', price: '', availability: false });
      toast({
        title: 'Success',
        description: 'New dish added.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error(error);
      toast({
        title: 'Error',
        description: 'Failed to add new dish. Please try again.',
        status: 'error',
        duration: 5000,
        isClosable: true,
      });
    }
  };

  return (
    <Box>
      <FormControl>
        <FormLabel>Search</FormLabel>
        <Input type="text" value={searchQuery} onChange={handleSearch} />
      </FormControl>

      <Table>
        <Thead>
          <Tr>
            <Th>Name</Th>
            <Th>Price</Th>
            <Th>Availability</Th>
          </Tr>
        </Thead>
        <Tbody>
          {/* {menu?.filter((dish) => dish.dish_name.toLowerCase().includes(searchQuery.toLowerCase()))
            .map((dish) => (
              <Tr key={dish.dish_id}>
                <Td>{dish.dish_name}</Td>
                <Td>{dish.price}</Td>
                <Td>
                  <Switch
                    isChecked={dish.availability}
                    onChange={(e) => handleAvailabilityToggle(dish.dish_id, e.target.checked)}
                  />
                </Td>
              </Tr>
            ))} */}
        </Tbody>
      </Table>

      <FormControl>
        <FormLabel>Add Dish</FormLabel>
        <Input
          type="text"
          placeholder="Dish Name"
          value={newDish.dish_name}
          onChange={(e) => setNewDish({ ...newDish, dish_name: e.target.value })}
        />
        <Input
          type="number"
          placeholder="Price"
          value={newDish.price}
          onChange={(e) => setNewDish({ ...newDish, price: e.target.value })}
        />
        <Switch
          isChecked={newDish.availability}
          onChange={(e) => setNewDish({ ...newDish, availability: e.target.checked })}
        />
        <Button onClick={handleAddDish}>Add</Button>
      </FormControl>
    </Box>
  );
};

export default Home;
