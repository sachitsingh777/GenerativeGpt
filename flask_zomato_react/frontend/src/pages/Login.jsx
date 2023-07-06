import React, { useState } from 'react';
import axios from 'axios';
import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Text,
  Center,
  Image,
} from '@chakra-ui/react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async () => {
    setError('');
    setIsLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/login', {
        username: username,
        password: password,
      });

      // Handle successful login
      console.log(response.data);
    } catch (error) {
      // Handle login error
      setError('Invalid username or password');
    }

    setIsLoading(false);
  };

  return (
    <Center height="100vh" backgroundColor="gray.100">
      <Box
        width="400px"
        p={6}
        borderRadius="md"
        backgroundColor="white"
        boxShadow="md"
      >
        <Center mb={6}>
          <Image src="zomato-logo.png" alt="Zomato Logo" height="40px" />
        </Center>
        <Stack spacing={4}>
          <FormControl id="username" isRequired>
            <FormLabel>Username</FormLabel>
            <Input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </FormControl>

          <FormControl id="password" isRequired>
            <FormLabel>Password</FormLabel>
            <Input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </FormControl>

          {error && <Text color="red.500">{error}</Text>}

          <Button
            colorScheme="teal"
            onClick={handleLogin}
            isLoading={isLoading}
            width="full"
          >
            Login
          </Button>
        </Stack>
      </Box>
    </Center>
  );
};



export  default Login
