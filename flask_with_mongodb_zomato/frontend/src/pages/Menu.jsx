import { useState, useEffect } from 'react';
import {
  Box,
  Heading,
  Input,
  Button,
  FormControl,
  FormLabel,
  Select,
  FormHelperText,
  Image,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  useDisclosure,
} from '@chakra-ui/react';
import { Link } from 'react-router-dom';



const Menu = () => {
  const [menu, setMenu] = useState([]);
  const [dishId, setDishId] = useState('');
  const [dishName, setDishName] = useState('');
  const [price, setPrice] = useState('');
  const [availability, setAvailability] = useState('');
  const [image, setImage] = useState(null);

  const { isOpen, onOpen, onClose } = useDisclosure();

  useEffect(() => {
    fetchMenuData();
  }, []);

  const fetchMenuData = async () => {
    try {
      const response = await fetch('http://localhost:5000/menu');
      const menuData = await response.json();
      setMenu(menuData);
    } catch (error) {
      console.log('Error fetching menu data:', error);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (name === 'dishId') {
      setDishId(value);
    } else if (name === 'dishName') {
      setDishName(value);
    } else if (name === 'price') {
      setPrice(value);
    } else if (name === 'availability') {
      setAvailability(value);
    }
  };

  const handleImageChange = (event) => {
    setImage(event.target.value);
  };

  const addDish = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('dish_id', dishId);
    formData.append('dish_name', dishName);
    formData.append('price', price);
    formData.append('availability', availability);
    formData.append('image', image);

    try {
      const response = await fetch('http://localhost:5000/add_dish', {
        method: 'POST',
        body: formData,
      });
      const menuData = await response.json();
      setMenu(menuData);
      // Reset form fields
      setDishId('');
      setDishName('');
      setPrice('');
      setAvailability('');
      setImage(null);
      onClose(); // Close the modal after adding the dish
    } catch (error) {
      console.log('Error adding dish:', error);
    }
  };

  const removeDish = async (dishId) => {
    try {
      const response = await fetch('http://localhost:5000/remove_dish', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ dish_id: dishId }),
      });
      const menuData = await response.json();
      setMenu(menuData);
    } catch (error) {
      console.log('Error removing dish:', error);
    }
  };

  return (
    <Box p={4}>
      <Heading as="h2" size="xl" mb={4}>
        Menu
      </Heading>
    
      <Button onClick={onOpen} colorScheme="blue" mb={4}>
        Add Dish
      </Button>
      <Link to="/chatbot"><Button position="fixed" top="50px" right="20px">ChatBot</Button></Link>
        
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Add Dish</ModalHeader>
          <ModalCloseButton />
          <form onSubmit={addDish}>
            <ModalBody>
              <FormControl mb={4}>
                <FormLabel>Dish ID</FormLabel>
                <Input
                  type="text"
                  name="dishId"
                  value={dishId}
                  onChange={handleInputChange}
                  placeholder="Dish ID"
                />
              </FormControl>

              <FormControl mb={4}>
                <FormLabel>Dish Name</FormLabel>
                <Input
                  type="text"
                  name="dishName"
                  value={dishName}
                  onChange={handleInputChange}
                  placeholder="Dish Name"
                />
              </FormControl>

              <FormControl mb={4}>
                <FormLabel>Price</FormLabel>
                <Input
                  type="text"
                  name="price"
                  value={price}
                  onChange={handleInputChange}
                  placeholder="Price"
                />
              </FormControl>

              <FormControl mb={4}>
                <FormLabel>Availability</FormLabel>
                <Select
                  name="availability"
                  value={availability}
                  onChange={handleInputChange}
                  placeholder="Select availability"
                >
                  <option value="yes">Yes</option>
                  <option value="no">No</option>
                </Select>
                <FormHelperText>
                  Select the availability of the dish
                </FormHelperText>
              </FormControl>

              <FormControl mb={4}>
                <FormLabel>Image</FormLabel>
                <Input
                  type="text"
                  name="image"
                  value={image}
                  onChange={handleImageChange}
                />
              </FormControl>
            </ModalBody>

            <ModalFooter>
              <Button type="submit" colorScheme="blue" mr={3}>
                Add Dish
              </Button>
              <Button onClick={onClose}>Cancel</Button>
            </ModalFooter>
          </form>
        </ModalContent>
      </Modal>

      {menu.map((dish) => (
        <Box key={dish._id} border="1px" p={4} mt={4}>
          <p>{dish.dish_name}</p>
          <p>{dish.price}</p>
          <p>{dish.availability ? 'Available' : 'Not Available'}</p>
          {dish.image && <Image src={dish.image} alt={dish.dish_name} />}
          <Button onClick={() => removeDish(dish._id)} colorScheme="red" mt={4}>
            Remove
          </Button>
        </Box>
      ))}

      {/* Add the Chatbot component */}
     
    </Box>
  );
};

export default Menu;
