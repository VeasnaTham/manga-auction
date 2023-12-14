import Navigation from "./Navigation/Nav";
import Books from "./Books/Books";
import Recommended from "./Recommended/Recommended";
import Sidebar from "./Sidebar/Sidebar";
import Card from "./components/Card";
import "./index.css";

import { useState } from "react";

import books from "./db/data";

function App() {
  const [selectedCategory, setSelectedCategory] = useState(null);

  // ----------- Input Filter -----------
  const [query, setQuery] = useState("");

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const filteredItems = books.filter(
    (book) => book.title.toLowerCase().indexOf(query.toLowerCase()) !== -1
  );

  // ----------- Radio Filtering -----------
  const handleChange = (event) => {
    setSelectedCategory(event.target.value);
  };

  // ------------ Button Filtering -----------
  const handleClick = (event) => {
    setSelectedCategory(event.target.value);
  };

  function filteredData(books, selected, query) {
    let filteredBooks = books;

    // Filtering Input Items
    if (query) {
      filteredBooks = filteredItems;
    }

    // Applying selected filter
    if (selected) {
      filteredBooks = filteredBooks.filter(
        ({ genre, category, price, title }) =>
          genre === selected ||
          category === selected ||
          price === selected ||
          title === selected
      );
    }

    return filteredBooks.map(({ img, title, price }) => (
      <Card 
      key={Math.random()} 
      img={img} 
      title={title} 
      price={price} />
    ));
  }

  const result = filteredData(books, selectedCategory, query);

  return (
    <>
      <Sidebar handleChange={handleChange} />
      <Navigation query={query} handleInputChange={handleInputChange} />
      <Recommended handleClick={handleClick} />
      <Books result={result} />
    </>
  );
}

export default App;
