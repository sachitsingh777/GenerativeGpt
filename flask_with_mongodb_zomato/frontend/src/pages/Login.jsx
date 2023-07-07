import { useState } from 'react';import {  Box,  Button,  FormControl,  FormErrorMessage,  FormLabel,  Heading,  Input,  Text,  useToast,} from '@chakra-ui/react';import { useNavigate } from 'react-router-dom';import './Login.css';const Login = () => {  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const toast = useToast();
  const navigate = useNavigate();

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error);
      }

      let data = await response.json();
      console.log(data);

      // Store user details except password in local storage
      localStorage.setItem('user', JSON.stringify(data.user));

      toast({
        title: 'Login Successful',
        description: 'You have successfully logged in.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });

      // Navigate to menu page
      navigate('/');

      // Perform any additional logic after successful login
    } catch (err) {
      setError(err.message);
      toast({
        title: 'Login Error',
        description: err.message,
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
      console.log(err);
    }
  };

  return (
    <Box bg="#3D3B3B" h="100vh" p="20">
    <Box
      maxW="sm"
      mx="auto"
      // mt={8}
      p={20}
      borderWidth={1}
      borderRadius="lg"
      position="relative"
      boxShadow="0 0 8px rgba(0, 0, 0, 0.1)"
      bg="#7A1B1B" // Light red transparent color
      backdropFilter="blur(8px)"
    >
      <Box
        position="absolute"
        top={0}
        left={0}
        width="100%"
        height="100%"
        // backdropFilter="blur(8px)"
      />
      <Heading as="h2" mb={4} textAlign="center" color="white">
        Login
      </Heading>
      <FormControl isInvalid={error}>
        <FormLabel color="white">Email:</FormLabel>
        <Input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          bg="white"
          borderBottom="1px solid rgba(255, 255, 255, 0.4)"
          borderRadius={0}
          color="black"
          _focus={{
            borderBottomColor: 'crystal.cyan',
          }}
        />
        <FormLabel mt={2} color="white">Password:</FormLabel>
        <Input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          bg="white"
          borderBottom="1px solid rgba(255, 255, 255, 0.4)"
          borderRadius={0}
          color="black"
          _focus={{
            borderBottomColor: 'crystal.cyan',
          }}
        />
        <FormErrorMessage>{error}</FormErrorMessage>
        <Button
          colorScheme="red"
          mt={4}
          onClick={handleSubmit}
          _hover={{
            bg: 'red.500',
          }}
        >
          Login
        </Button>
      </FormControl>
    </Box>
    </Box>
  );
};

export default Login;