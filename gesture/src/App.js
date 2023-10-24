import "./index.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import SelectMenu from "./component/SelectMenu";
import Volume from "./component/Volume";
import Screen from "./component/Screen";

function App() {
  return (
    <BrowserRouter>
      <div className="bg-black h-screen font-Pretendard">
        <Routes>
          <Route path="/" element={<SelectMenu />}></Route>
          <Route path="/volume" element={<Volume />}></Route>
          <Route path="/screen" element={<Screen />}></Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
