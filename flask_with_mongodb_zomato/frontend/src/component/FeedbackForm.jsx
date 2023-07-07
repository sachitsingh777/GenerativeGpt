import { useState } from 'react';
import { Button, FormControl, FormLabel, Input, VStack } from '@chakra-ui/react';

const FeedbackForm = ({ onFeedbackSubmit }) => {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onFeedbackSubmit(feedback);
    setFeedback('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <VStack spacing={4} align="flex-start">
        <FormControl id="feedback">
          <FormLabel>Feedback</FormLabel>
          <Input
            type="text"
            value={feedback}
            onChange={(event) => setFeedback(event.target.value)}
            required
          />
        </FormControl>
        <Button type="submit" colorScheme="blue">
          Submit Feedback
        </Button>
      </VStack>
    </form>
  );
};

export default FeedbackForm;
