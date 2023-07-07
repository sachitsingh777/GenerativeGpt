import { useState, useEffect } from 'react';
import { Button, FormControl, FormLabel, Input, VStack } from '@chakra-ui/react';
import FeedbackForm from './FeedbackForm';
import FeedbackList from './FeedbackList';

const Feedback = () => {
  const [username, setUsername] = useState('');
  const [feedbacks, setFeedbacks] = useState([]);

  useEffect(() => {
    // Fetch the initial feedbacks from the server
    const fetchFeedbacks = async () => {
      try {
        const response = await fetch('/api/feedbacks');
        const data = await response.json();
        setFeedbacks(data.feedbacks);
      } catch (error) {
        console.error('Error:', error);
        // Handle the error
      }
    };

    fetchFeedbacks();
  }, []);

  const handleLogin = async (event) => {
    event.preventDefault();
    // Here you would typically make a POST request to authenticate the user
    // and handle the login response.
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
      });
      const data = await response.json();
      console.log(data);
      if (data.success) {
        localStorage.setItem('username', data.username);
      }
      // Handle the response as needed
    } catch (error) {
      console.error('Error:', error);
      // Handle the error
    }
  };

  const handleFeedbackSubmit = async (feedback) => {
    const username = localStorage.getItem('username');
    const payload = { feedback, username };
    try {
      const response = await fetch('/feedback',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      console.log(data);
      if (data.success) {
        // Add the new feedback to the feedbacks state
        setFeedbacks([...feedbacks, { username, feedback }]);
      }
      // Handle the response as needed
    } catch (error) {
      console.error('Error:', error);
      // Handle the error
    }
  };

  return (
    <VStack spacing={4} align="center" p={4}>
      {localStorage.getItem('username') ? (
        <>
          <FeedbackForm onFeedbackSubmit={handleFeedbackSubmit} />
          <FeedbackList feedbacks={feedbacks} />
        </>
      ) : (
        <form onSubmit={handleLogin}>
          <VStack spacing={4} align="flex-start">
            <FormControl id="username">
              <FormLabel>Username</FormLabel>
              <Input
                type="text"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                required
              />
            </FormControl>
            <Button type="submit" colorScheme="blue">
              Log In
            </Button>
          </VStack>
        </form>
      )}
    </VStack>
  );
};

export default Feedback;
