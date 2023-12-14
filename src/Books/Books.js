import "./Books.css";

const Books = ({ result }) => {
  return (
    <>
      <section className="card-container">{result}</section>
    </>
  );
};

export default Books;