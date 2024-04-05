import { createAuthProvider } from 'react-token-auth';

type Session = { access_token: string; refresh_token: string };

export const { useAuth, authFetch, login, logout } = createAuthProvider<Session>({
    getAccessToken: session => session.access_token,
    storage: localStorage,
    onUpdateToken: token =>
        fetch('http://127.0.0.1:5000/auth/refresh', {
            method: 'POST',
            body: token.refresh_token,
        }).then(r => r.json()),
});