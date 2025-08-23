import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Page from './app/login/page';
import { UserPanel } from './components/user-panel';
import { TeacherPanel } from './components/teacher-panel';
import { SuperUserPanel } from './components/superuser-panel';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <BrowserRouter>
      <div className="flex min-h-screen w-full items-center justify-center p-6 md:p-10">
        <div className="w-full max-w-sm">
          <Routes>
            <Route path="/" element={<Page />} />
            <Route element={<ProtectedRoute />}>
              <Route path="/userpanel" element={<UserPanel />} />
              <Route path="/teacherpanel" element={<TeacherPanel />} />
              <Route path="/superuserpanel" element={<SuperUserPanel />} />
            </Route>
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
