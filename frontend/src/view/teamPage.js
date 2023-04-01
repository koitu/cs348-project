
import React, { useEffect , useState } from "react"
import { useParams } from "react-router-dom"

export function TeamDetailedPage() {
    let { id } = useParams()
    return (
        <p>
            this is detailed webpage for team with {id}
        </p>
    )
}