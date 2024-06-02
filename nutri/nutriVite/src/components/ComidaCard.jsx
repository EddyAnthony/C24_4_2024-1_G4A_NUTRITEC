import { useNavigate } from 'react-router-dom';

export function ComidaCard({ comida }) {
    const navigate = useNavigate();

    return (
        <div className='bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer'
             onClick={() => navigate(`/comida/${comida.id}`)}>
            <h1>{comida.nombre}</h1>
            <p>{comida.categoria.nombre}</p>
        </div>
    );
}
