import React from 'react';
import {
  Box,
  Flex,
  Text,
  Spacer,
  useDisclosure,
  Collapse,
} from '@chakra-ui/react';
import { Link } from 'react-router-dom';

const Navbar = ({ isLoggedIn, username, onLogout }) => {
  const { isOpen, onToggle } = useDisclosure();

  return (
    <Box bg="teal.500" px={4} py={2}>
      <Flex alignItems="center">
        <Link to="/">
          <Text color="white" fontWeight="bold" fontSize="xl">
            Logo
          </Text>
        </Link>
        <Spacer />
        <Box display={{ base: 'none', md: 'flex' }}>
          <Link to="/">
            <Text color="white" mx={2}>
              Menu
            </Text>
          </Link>
          <Link to="/order">
            <Text color="white" mx={2}>
              Order
            </Text>
          </Link>
          <Flex justifyContent="flex-end" mt={2}>
        {isLoggedIn ? (
          <Flex >
            <Text color="white" mr={2}>
              {username}
            </Text>
            <Text  colorScheme="teal" size="sm" onClick={onLogout}>
              Logout
            </Text >
          </Flex>
        ) : (
          <Flex alignItems="center">
            <Link to="/login">
              <Text  colorScheme="teal" size="sm" mr={2}>
                Login
              </Text >
            </Link>
            <Link to="/signup">
              <Text  colorScheme="teal" size="sm">
                Signup
              </Text >
            </Link>
          </Flex>
        )}
      </Flex>
        </Box>
        <Text 
          colorScheme="teal"
          size="sm"
          onClick={onToggle}
          display={{ base: 'block', md: 'none' }}
        >
          Menu
        </Text >
      </Flex>
      <Collapse in={isOpen} animateOpacity>
        <Box mt={2}>
          <Flex flexDirection="column" alignItems="center">
            <Link to="/">
              <Text color="white" my={2}>
                Menu
              </Text>
            </Link>
            <Link to="/order">
              <Text color="white" my={2}>
                Order
              </Text>
            </Link>
            <Link to="/orderdetails">
              <Text color="white" my={2}>
                Order Status
              </Text>
            </Link>
          </Flex>
          <Flex justifyContent="flex-end" mt={2}>
        {isLoggedIn ? (
          <Flex alignItems="center">
            <Text color="white" mr={2}>
              {username}
            </Text>
            <Text  colorScheme="teal" size="sm" onClick={onLogout}>
              Logout
            </Text >
          </Flex>
        ) : (
          <Flex alignItems="center">
            <Link to="/login">
              <Text size="sm" mr={2}>
                Login
              </Text >
            </Link>
            <Link to="/signup">
              <Text  colorScheme="teal" size="sm">
                Signup
              </Text >
            </Link>
          </Flex>
        )}
      </Flex>
        </Box>
      </Collapse>
      
    </Box>
  );
};

export default Navbar;
