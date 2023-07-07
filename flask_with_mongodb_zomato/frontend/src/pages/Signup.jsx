import React, { useState } from 'react';
import { Box, Button, FormControl, FormLabel, Heading, Input, Select, useToast } from '@chakra-ui/react';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');
    const [email, setEmail] = useState('');
    const toast = useToast();


    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:5000/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password, role, email }),
            });

            if (response.ok) {
              
                let data = await response.json()
                console.log(data)
                toast({
                    title: 'Signup Successful',
                    status: 'success',
                    duration: 3000,
                    isClosable: true,
                  });
            } else {
            
                const errorData = await response.json();
                console.log('Signup error:', errorData.error);
                toast({
                    title: 'Signup Error',
                    description: errorData.error,
                    status: 'error',
                    duration: 3000,
                    isClosable: true,
                  });
            }
        } catch (error) {
            console.error('Error:', error);
            toast({
                title: 'Error',
                description: error.message,
                status: 'error',
                duration: 3000,
                isClosable: true,
              });
        }
    };

    return (
      <Box bg="#3D3B3B" h="100vh" p="5">
        <Box maxW="sm" mx="auto" mt={8} p={4} borderWidth={1} bg="#7A1B1B" borderColor="red.600" borderRadius="md">
            <Heading as="h2" mb={4} textAlign="center">
                Signup
            </Heading>
            <form onSubmit={handleSubmit} bg="white">
                <FormControl id="username" mb={4}>
                    <FormLabel>Username:</FormLabel>
                    <Input
                   bg="whiteAlpha.500"
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        variant="outline"
                    />
                </FormControl>
                <FormControl id="email" mb={4}>
                    <FormLabel>Email:</FormLabel>
                    <Input
                      bg="whiteAlpha.500"
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        variant="outline"
                    />
                </FormControl>
                <FormControl id="password" mb={4}>
                    <FormLabel>Password:</FormLabel>
                    <Input
                      bg="whiteAlpha.500"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        variant="outline"
                    />
                </FormControl>
                <FormControl id="role" mb={4}>
                    <FormLabel>Role:</FormLabel>
                    <Select value={role} onChange={(e) => setRole(e.target.value)} variant="outline"   bg="whiteAlpha.500">
                        <option value="">Select Role</option>
                        <option value="admin">Admin</option>
                        <option value="user">User</option>
                    </Select>
                </FormControl>

                <Button type="submit" colorScheme="red" size="lg" w="100%">
                    Sign Up
                </Button>
            </form>
        </Box>
        </Box>
    );
};

export default Signup;
