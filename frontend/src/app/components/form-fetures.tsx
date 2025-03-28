// import React, { ChangeEvent } from 'react';

// interface InputProps {
//     type?: string;
//     id: string;
//     label?: string;
//     placeholder?: string;
//     value?: string;
//     onChange?: (event: ChangeEvent<HTMLInputElement>) => void;
//     required?: boolean;
// }

// const Input: React.FC<InputProps> = ({
//     type = 'text',
//     id,
//     label,
//     placeholder,
//     value,
//     onChange,
//     required,
// }) => {
//     return (
//         <div className="mb-4">
//             {label && <label htmlFor={id} className="block text-gray-700 text-sm font-bold mb-2">{label}</label>}
//             <input
//                 type={type}
//                 id={id}
//                 placeholder={placeholder}
//                 value={value}
//                 onChange={onChange}
//                 required={required}
//                 className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
//             />
//         </div>
//     );
// };
// export default Input;