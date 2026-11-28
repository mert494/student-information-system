import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { CourseListPreview } from './CourseListPreview';

const root = document.getElementById('root');
if (!root) throw new Error('Missing course preview root');
createRoot(root).render(<StrictMode><CourseListPreview /></StrictMode>);
