import { useState } from 'react';
export default function CheckoutForm(){
  const [addr,setAddr] = useState({line1:'',city:'',postal:''});
  return (
    <form>
      <input placeholder='Address line 1' value={addr.line1} onChange={e=>setAddr({...addr,line1:e.target.value})}/>
      <input placeholder='City' value={addr.city} onChange={e=>setAddr({...addr,city:e.target.value})}/>
      <input placeholder='Postal' value={addr.postal} onChange={e=>setAddr({...addr,postal:e.target.value})}/>
    </form>
  );
}
