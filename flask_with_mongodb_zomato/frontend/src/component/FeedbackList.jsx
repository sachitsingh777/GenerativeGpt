import { VStack, Box, Text } from '@chakra-ui/react';

const FeedbackList = ({ feedbacks }) => {
  return (
    <VStack spacing={4} align="flex-start" mt={4}>
      {feedbacks.map((feedback, index) => (
        <Box key={index} p={4} borderWidth="1px" borderRadius="md">
          <Text fontWeight="bold">{feedback.username}</Text>
          <Text>{feedback.feedback}</Text>
        </Box>
      ))}
    </VStack>
  );
};

export default FeedbackList;
