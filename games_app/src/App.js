import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import games from './data/games.json';

function App() {
  return (
    <Container className='mt-4'>
      <Row>
        {games?.map((game, index) => {
          return (
            <Col md={4} className='mt-4' key={index}>
              <Card>
                <Card.Body>
                  <Card.Title>{game.title}</Card.Title>
                  <Card.Text>Price: {game.price}</Card.Text>
                  <Button variant="primary">View More</Button>
                </Card.Body>
              </Card>
            </Col>
          );
        })}
      </Row>
    </Container>
  );
}

export default App;